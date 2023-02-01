const gametime = 180;
const countimgs = ['no1.png','no2.png','no3.png','no4.png','no5.png'];

var Math = Math || {};
Math.type = 'idiom';
Math.Level = 'degree1';
Math.mode = 'exam'; //'practice'
Math.broadcast = 'random'; //'sequence'
Math.timer;
Math.precount = 6;
Math.gamecount = gametime;

Math.words = ['Test'];
Math.qIndex = 0;
Math.examlist = [];

Math.correct = 0;
Math.error = 0;
Math.score = 0;

Math.Init = function () {
    Math.Reset();

    let formdata = {};
    formdata.Game = Math.type;
    formdata.Level = Math.Level;
    if (Math.broadcast == 'random') {
        formdata.GameType = "隨機";
    } else {
        formdata.GameType = "依序";
    }
    if (Math.mode == 'exam') {
        formdata.Mode = '測驗';
    } else {
        formdata.Mode = '練習';
    }
    Game.Start(formdata, function (id) {
        $("button[name=start]").attr("game-id", id);
    });

    $("button[name=start]").prop('disabled', true);
    $("#library button").prop('disabled', true);
    $("input[type=radio][name=mode]").prop('disabled', true);
    $("input[type=radio][name=broadcast]").prop('disabled', true);

    Math.examlist = [];

    $("#result").prop('disabled', false);
    $("#result").unbind();
    $("#result").bind('keydown', function (e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            e.stopPropagation();
            $(this).trigger(jQuery.Event("change"));
        }
    });
    $("#result").bind('change', function () {
        if ($("#result").val() === $("#result").attr("ans")) {
            $("audio")[1].play();
            Math.correct += 1;
            Math.score += 100;
            Math.shownext();
            $("#result").val('').focus().select();
        } else {
            $("audio")[2].play();
            Math.error += 1;
            Math.score -= 7;
            if (Math.score < 0) {
                Math.score = 0;
            }
            $("#result").focus().select();
        }
        $("#score").html("Score :" + Math.score);
        if (Math.mode == 'practice') {
            Math.updateLog(0);
        }
    });

	Math.precount = 6;
	Math.countdown();
}

Math.Reset = function () {
    Math.qIndex = 0;
    Math.correct = 0;
    Math.error = 0;
    Math.score = 0;
    $("div.character").html('');
    $("abbr[name=time]").html(gametime);
    $("abbr[name=score]").html(0);
    $("abbr[name=time]").html(gametime);

    $("div.character").html('');
    $("#result").val('');

    $("#library button").prop('disabled', false);
    $("input[type=radio][name=mode]").prop('disabled', false);
    $("input[type=radio][name=broadcast]").prop('disabled', false);
};

Math.countdown = function () {
	$("#work_area").hide();
    $("div.lmask").show();
	Math.precount -= 1;
	if(Math.precount > 0) {
        $("div.lmask").html("<img src='static/imgs/" + countimgs[Math.precount - 1] + "' width='500' height='500' />");
	}
	$("audio")[0].play();
	if(Math.precount > 0){
		Math.timer  = setTimeout(Math.countdown, 1000);
    } else {
        $("div.lmask").hide();
		$("#work_area").show();
        Math.shownext();
        $("i.fa-volume-up").bind('click', function () {
            $("audio")[4].play();
            $("#result").val('').focus().select();
        });
        $("#result").prop('disabled', false);
		$("#result").focus().select();
		Math.gamecount = gametime;
		Math.score = 0;
		Math.gametiming();
	}
}

Math.gametiming = function(){
	Math.gamecount -= 1;
	 $("abbr[name=time]").html(Math.gamecount);
	if(Math.gamecount > 0){
	  Math.timer  = setTimeout(Math.gametiming, 1000);
	}else{
		Math.gameover ();
	}
}

Math.shownext = function () {
    i = Math.floor(Math.random() * 8) + 2;
	j = Math.floor(Math.random() * 9) + 1;
	faudio = i + "X" + j;
	
	$("#ch1").html(i);
	$("#ch2").html(j);
	$("#result").attr("ans", i * j);
	
	$("audio")[4].src = "static/pronunc/" + faudio + ".mp3";
	$("audio")[4].play();

    if (Math.broadcast == 'sequence') {
        Math.qIndex += 1;
        if (Math.qIndex >= Math.words.length) {
            Math.qIndex = 0;
        }
    }
};

Math.gameover = function () {
    $("button[name=start]").prop('disabled', false);
    $("#library button").prop('disabled', false);
    $("#result").prop('disabled', true);
    $("#result").unbind();
    $("audio")[3].play();

    Math.updateLog(180);
    $("button[name=start]").attr("game-id", "");

    var shareurl = "/player/" + Math.score;
    //show share dialog
    $("#scoreshare").on('show.bs.modal', function () {
        $("#scoreshare iframe").attr("src", shareurl);
        $("#playerId").val("");
    });
    $("#scoreshare").on('shown.bs.modal', function () {
        var scale = $("#scoreshare div.modal-body").width() / 480;
        $("#scoreshare iframe").css("transform", "scale(" + scale + ")");
        $("#scoreshare div.modal-body").height(scale * 700);
    });
    $("#scoreshare").on('hidden.bs.modal', function () {
        if ($("#playerId").val() !== "") {
            let formdata = {};
            formdata.PlayerID = $("#playerId").val();
            formdata.Game = Math.type;
            formdata.Level = Math.Level;
            if (Math.broadcast == 'random') {
                formdata.GameType = "隨機";
            } else {
                formdata.GameType = "依序";
            }
            formdata.Question = Math.correct;
            formdata.Wrong = Math.error;
            formdata.FinalScore = Math.score;
            Game.SaveScore(formdata);
        }
        Math.Reset();
    });


    $("#scoreshare").modal({
        backdrop: 'static',
        keyboard: false
    });
    $("#scoreshare").modal("show");

    Math.timer = setTimeout(function () {
        $("div.character").html("");
    }, 3000);
};

Math.updateLog = function (time) {
    let id = $("button[name=start]").attr("game-id");
    if (id !== undefined && id !== "") {
        let formdata = {};
        formdata.ID = $("button[name=start]").attr("game-id");
        formdata.Question = Math.correct;
        formdata.Wrong = Math.error;
        formdata.FinalScore = Math.score;
        formdata.GameTime = time;
        Game.Finished(formdata);
    }
};

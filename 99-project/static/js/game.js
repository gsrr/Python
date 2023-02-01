var Game = Game || {};

Game.SaveScore = function (param, callback, errorCallback) {
    param.CreateTime = new Date().Format("yyyy-MM-dd hh:mm:ss");
    $.ajax({
        type: 'POST',
        url: "/api/score",
        data: param,
        success: function (response, status, xhr) {
            if (callback && typeof (callback) === "function") {
                callback(response);
            }
        },
        error: function (xhr) {
            if (errorCallback && typeof (errorCallback) === "function") {
                errorCallback(xhr)
            }
        }
    });
};

Game.Start = function (param, callback, errorCallback) {
	/*
    param.StartTime = new Date().Format("yyyy-MM-dd hh:mm:ss");
    $.ajax({
        type: 'POST',
        url: "/api/gamelog",
        data: param,
        success: function (response, status, xhr) {
            if (callback && typeof (callback) === "function") {
                callback(response);
            }
        },
        error: function (xhr) {
            if (errorCallback && typeof (errorCallback) === "function") {
                errorCallback(xhr)
            }
        }
    });
	*/
};

Game.Finished = function (param, callback, errorCallback) {
    param.EndTime = new Date().Format("yyyy-MM-dd hh:mm:ss");
    $.ajax({
        type: 'PUT',
        url: "/api/gamelog",
        data: param,
        success: function (response, status, xhr) {
            if (callback && typeof (callback) === "function") {
                callback(response);
            }
        },
        error: function (xhr) {
            if (errorCallback && typeof (errorCallback) === "function") {
                errorCallback(xhr)
            }
        }
    });
};
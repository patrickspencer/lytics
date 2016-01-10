var lyticsApp = angular.module('lyticsApp', []);

lyticsApp.controller('ExpenditureCtrl', function($scope, $http) {
    if ($scope.search == undefined) {
        $scope.search = "Sherlock Holmes";
        fetch();
    }
    function fetch() {
        $http.get("http://www.omdbapi.com/?t=" + $scope.search +
                  "&tomatoes=true&plot=full")
            .success(function(response) {
                $scope.details = response;
        });
    };
});

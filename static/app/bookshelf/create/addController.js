angular.module('bookshelf.list').controller('addController', ['$mdDialog', '$mdToast', '$filter', 'resource', '$scope', 
                                 function ($mdDialog, $mdToast, $filter, resource, $scope) {
    'use strict';
    var ctrl = this;
    ctrl.cancel = $mdDialog.cancel;
  
    function success() {
        $mdDialog.hide();
    };
    
    function error(result) {
        $mdToast.show(
            $mdToast.simple({
                position: "bottom right",
                hideDelay: 200000,
                template:  '<md-toast class="md-toast md-warn">' + result.data.errors + '</md-toast>'
            })
        )
    };

    ctrl.reset = function() {
        $scope.book = {
            title: "",
            author: "",
            publishdate: "",
            description: "",
            cover: ""
        }
    };
    ctrl.submit = function() {
        if ($scope.fileName) {
            $scope.book.cover = $scope.file;
        }
        $scope.book.publishdate = $filter('date')(Date.parse($scope.book.publishdate), 'yyyy-MM-dd');
        resource.saveBook($scope.book).$promise.then(success, error);
    };
}]);

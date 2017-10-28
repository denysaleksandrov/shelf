angular.module('bookshelf.list').controller('updateController', ['book', 'books', '$mdDialog', '$mdToast', '$filter', 'resource', '$scope',
                                 function (book, books, $mdDialog, $mdToast, $filter, resource, $scope) {
    'use strict';
    var ctrl = this;
    ctrl.book = {};
    ctrl.book.title = book.title;
    ctrl.book.author= book.author;
    ctrl.book.publishdate = new Date(Date.parse(book.publishdate));
    ctrl.book.description = book.description;
    ctrl.cancel = $mdDialog.cancel;

    function error(result) {
        $mdToast.show(
            $mdToast.simple()
            .textContent(result.data.errors)
            .position("bottom right")
            .hideDelay(2000)
            .theme("error-toast")
        )
    };

    function success() {
        books.length = 0;
        $mdDialog.hide();
    } 
  
    ctrl.submit = function() {
        if ($scope.fileName) { 
            ctrl.book.cover = $scope.file;
        }
        ctrl.book.publishdate = $filter('date')(Date.parse(ctrl.book.publishdate), 'yyyy-MM-dd');
        resource.updateBook({id: book.id}, ctrl.book).$promise.then(success, error);
    };
}]);

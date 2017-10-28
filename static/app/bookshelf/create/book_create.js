angular.module('bookshelf.list')
.controller('addController', ['$mdDialog', 'resource', '$scope', 
                              function ($mdDialog, resource, $scope) {
  'use strict';

  this.cancel = $mdDialog.cancel;
  
  function success() {
    $mdDialog.hide($scope.book);
  }
  
  function reset() {
    $scope.book = {
        title: "",
        author: "",
        publishdate: "",
        description: ""
    }
  };
    //srv.submit = function() {
    //    srv.book.publishdate = $filter('date')(Date.parse(srv.book.publishdate), 'yyyy-MM-dd');
    //    resource.saveBook(srv.book).$promise.then(function(data) {
    //        srv.messages.push("Book " + srv.book.title + " created.");
    //        srv.showToast(srv.messages, 'success');
    //        $mdDialog.hide();
    //    }, function(error) {
    //        console.log(error);
    //        angular.forEach(error.data, function(field, errors) {
    //            srv.messages.push(field)
    //        });
    //        srv.showToast(srv.messages, 'error');
    //    });
    //};
  this.addBook = function () {
    console.log('ASD');
    console.log($scope.book);
  };
}]);

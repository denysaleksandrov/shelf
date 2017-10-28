angular.module('bookshelf.list').controller('deleteController', ['books', '$mdDialog', 'resource', '$q', 
                                 function (books, $mdDialog, resource, $q) {
  'use strict';
  var ctrl = this;
  ctrl.cancel = $mdDialog.cancel;
  
  function deleteBook(book, index) {
    var deferred = resource.deleteBook({id: book.id});
    deferred.$promise.then(function () {
      books.splice(index, 1);
    });
    
    return deferred.$promise;
  }
  
  function onComplete() {
    books.length = 0;
    $mdDialog.hide();
  }
  
  ctrl.success = function() {
    $q.all(books.forEach(deleteBook)).then(onComplete);
  }
  
}]);

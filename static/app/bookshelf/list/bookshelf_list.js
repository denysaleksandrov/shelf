angular.module('bookshelf.list', ['resource'])
.component('bookshelfList', {
    templateUrl: '/static/app/bookshelf/list/bookshelf_list.html',
    bindings: {
        books: '<',
    },
    controller: function($scope, $state, $filter, $mdDialog, $mdToast, resource) {
        var ctrl = this;
        ctrl.selected = [];
        ctrl.books = [];
        ctrl.limitOptions = [10, 20, 50];
        ctrl.book_count = 0;
        ctrl.options = {
          	rowSelection: true,
          	multiSelect: true,
          	autoSelect: false,
          	decapitate: false,
          	largeEditDialog: false,
          	boundaryLinks: true,
          	limitSelect: true,
          	pageSelect: true
        };
        ctrl.query = {
          order: 'title',
          limit: 20,
          page: 1
        };
        
        ctrl.addBook = function(event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                controller: 'addController',
                controllerAs: 'ctrl',
                focusOnOpen: false,  
                targetEvent: event,
                templateUrl: '/static/app/bookshelf/create/add-dialog.html',
            })
            .then(function() {
                ctrl.getBooks().then(ctrl.setBooks);
            })
            .then(function() {
                $mdToast.show(
                    $mdToast.simple()
                        .textContent('Book created.')
                        .position("bottom right")
                        .hideDelay(2000)
                        .theme("success-toast")
                    ).then(function() {
                        ctrl.getListToast();
                });
            });
        };

        ctrl.updateBook = function(event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                controller: 'updateController',
                controllerAs: 'ctrl',
                focusOnOpen: false,  
                targetEvent: event,
                locals: { book: ctrl.selected[0], books: ctrl.selected },
                templateUrl: '/static/app/bookshelf/update/update-dialog.html',
            })
            .then(function() {
                ctrl.getBooks().then(ctrl.setBooks);
            })
            .then(function() {
                $mdToast.show(
                    $mdToast.simple()
                        .textContent('Book updated.')
                        .position("bottom right")
                        .hideDelay(2000)
                        .theme("success-toast")
                )
            });
        };

        ctrl.deleteBooks = function(event) {
            $mdDialog.show({
                clickOutsideToClose: true,
                controller: 'deleteController',
                controllerAs: 'ctrl',
                focusOnOpen: false,
                targetEvent: event,
                locals: { books: ctrl.selected },
                templateUrl: '/static/app/bookshelf/delete/delete-dialog.html',
            })
            .then(function() {
                ctrl.getBooks().then(ctrl.setBooks);
            })
            .then(function() {
                $mdToast.show(
                    $mdToast.simple()
                        .textContent('Book(s) deleted.')
                        .position("bottom right")
                        .hideDelay(2000)
                        .theme("success-toast")
                    ).then(function() {
                        ctrl.getListToast();
                });
            });
        };
                
        ctrl.getListToast = function(result) {
            $mdToast.show(
                $mdToast.simple()
                    .textContent('Got ' + ctrl.book_count + ' book')
                    .position("bottom right")
                    .hideDelay(3000)
                    .theme("success-toast")
            )};

        ctrl.setBooks = function(result) {
            ctrl.books = result.books;
            ctrl.book_count = result.bookCount;
        };
        ctrl.getBooks = function() {
            return resource.books().$promise
        };

        ctrl.toggleLimitOptions = function() {
          ctrl.limitOptions = ctrl.limitOptions ? undefined : [10, 20, 50];
        };
        ctrl.onPaginate = function(page, limit) {
            resource.books({limit: limit, offset: (page-1) * limit}).$promise
                .then(function(result) {
                    ctrl.books = result.books;
                })
        }; 
        ctrl.getBooks().then(ctrl.setBooks).then(ctrl.getListToast);
    }
});

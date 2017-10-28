angular.module('service', ['resource'])
.service('service', ['$state', 'resource', '$mdToast', '$mdDialog', '$filter', 
    function($state, resource, $mdToast, $mdDialog, $filter) {
    var srv = this;
    srv.reset = function() {
        srv.book = {
            title: "",
            author: "",
            publishdate: "",
            description: ""
        }
    };
    srv.submit = function() {
        srv.messages = [];
        srv.book.publishdate = $filter('date')(Date.parse(srv.book.publishdate), 'yyyy-MM-dd');
        resource.saveBook(srv.book).$promise.then(function(data) {
            srv.messages.push("Book " + srv.book.title + " created.");
            srv.showToast(srv.messages, 'success');
            $mdDialog.hide();
        }, function(error) {
            console.log(error);
            angular.forEach(error.data, function(field, errors) {
                srv.messages.push(field)
            });
            srv.showToast(srv.messages, 'error');
        });
    };
    srv.querySearch = function(query, where) {
        var results = query ? where.filter(srv.createFilterFor(query)) : where;
        return results;
    }
    srv.createFilterFor = function(query) {
        return function filterFn(model) {
            return (model.name.search(new RegExp(query, "i")) >= 0);
        };
    };
    srv.showToast = function(message, type) {
        $mdToast.show(
            $mdToast.simple()
                .hideDelay(3000)
                .position('top center')
                .content(message)
                .theme(type + "-toast")
        );
    };
    srv.cancel = function() {
        $mdDialog.cancel();
    };
    srv.addBookMenu = function(ev) {
        $mdDialog.show({
            controller: function() { return srv; },
            controllerAs: 'srv',
            templateUrl: '/static/app/bookshelf/service/create_dialog.html', 
            targetEvent: ev,
            clickOutsideToClose:false
        });
    };
    function DialogController($scope, $mdDialog) {
        $scope.hide = function() {
            $mdDialog.hide();
        };
        $scope.cancel = function() {
            $mdDialog.cancel();
        };
        /*
        $scope.create = function(device) {
            if (device === 'junos_device') {
                $state.go('create');
                $mdDialog.hide();
            }
        };
        */
    }
}]);


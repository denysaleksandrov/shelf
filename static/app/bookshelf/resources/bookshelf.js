angular.module("resource", ['ngResource'])
.factory('resource', function($resource) {
    var actions = {
        'saveBook': {
            method: 'POST',
            url: '/api/bookshelf',
            transformRequest: function(data, headers) {
                req = {"book": data}
                return angular.toJson(req);
            }
        },
        'updateBook': {
            method: 'PUT',
            url: '/api/bookshelf/:id',
            transformRequest: function(data, headers) {
                req = {"book": data}
                return angular.toJson(req);
            }
        },
        'books': {
           method: 'GET',
           url: '/api/bookshelf',
           params: { limit: 20, offset:0 }
        },
        'deleteBook': {
            method: 'DELETE',
            url: '/api/bookshelf/:id'
        },
    };
    return $resource('/api/booskhelf', {}, actions);
})

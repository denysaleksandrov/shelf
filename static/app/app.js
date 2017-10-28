'use strict';

// Declare app level module which depends on views, and components
angular.module('bookshelf', [
    'ui.router',
    'ui.bootstrap',
    'ui.select',
    'ngResource',
    'ngSanitize',
    'ngMaterial',
    'ngAnimate',
    'ngMessages',
    'ngAria',
    'ngMdIcons',
    'md.data.table',
    'bookshelf.list',
    'resource',
    'service'
])
.config(['$resourceProvider', '$stateProvider', '$urlRouterProvider', '$httpProvider', '$mdThemingProvider',
    function($resourceProvider, $stateProvider, $urlRouterProvider, $httpProvider, $mdThemingProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        // Do not strip strailing slashes from URLs, django expects them.
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $mdThemingProvider.theme('success-toast');
        $mdThemingProvider.theme('default')
            .primaryPalette('blue');
        

        $urlRouterProvider.otherwise('/bookshelf');
        $stateProvider
            .state('bookshelf', {
                url: '/bookshelf',
                template: '<bookshelf-list></bookshelf-list>',
            });
    }
]);
 

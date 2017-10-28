angular.module('bookshelf.list').directive('apsUploadFile', ['$window', function($window) {
    return {
        restrict: 'E',
        templateUrl: '/static/app/bookshelf/upload/upload.html',
        link: function(scope, element, attrs) {
            var fileReader = new $window.FileReader();
            var input = angular.element(element[0].querySelector('input#fileInput'));
            var button = angular.element(element[0].querySelector('#uploadButton'));
            //var textInput = angular.element(element[0].querySelector('#textInput'));
        
            //if (input.length && button.length && textInput.length) {
            //    button.bind('click', function (e) {
            //        input.click();
            //    });
            //    textInput.bind.('click', function (e) {
            //        input.click();
            //    });
            //}
            button.bind('click', function () {
                input[0].click();
            });
            
            fileReader.onload = function() {
                scope.file = fileReader.result;
            };

            input.bind('change', function (e) {
                var files = e.target.files;
                if (files[0]) {
                    scope.fileName = files[0].name;
                    fileReader.readAsDataURL(files[0]);
                } else {
                    scope.fileName = null;
                }
                scope.$apply();
            });
        }
    }
}]);

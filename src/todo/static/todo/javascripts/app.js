if (!rootURL) {
    rootURL = '/';
    // if the rootURL is not initialized in the template,
    // it defaults to '/'
}

angular.module('nodeTodo', [])
.controller('mainController', ($scope, $http) => {
    $scope.formData = {};
    $scope.todoData = {};

    // Get all todos
    $http.get(rootURL + 'api/v1/get/')
    .then((data) => {
        $scope.todoData = data;
        console.log(data);
    },
    (error) => {
        console.log('Error: ' + error);
    });

    // Create a new todo
    $scope.createTodo = () => {
        // console.log($scope.formData);
        $http.post(rootURL + 'api/v1/add/', $scope.formData)
        .then((data) => {
            $scope.formData = {};
            $scope.todoData = data;
            console.log(data);
        },
        (error) => {
            console.log('Error: ' + error);
        });
    };

    // Update todo
    $scope.updateTodo = (todo) => {
        // console.log(!todo.complete);
        $http.put(rootURL + 'api/v1/update/' + todo.id + '/', {"text": todo.text, "complete": !todo.complete})
        .then((data) => {
            $scope.todoData = data;
            console.log(data);
        },
        (error) => {
            console.log('Error: ' + error);
        });
    };

    // Delete a todo
    $scope.deleteTodo = (todoID) => {
        $http.delete(rootURL + 'api/v1/delete/' + todoID + '/')
        .then((data) => {
            $scope.todoData = data;
            console.log(data);
        },
        (error) => {
            console.log('Error: ' + error);
        });
    };
});

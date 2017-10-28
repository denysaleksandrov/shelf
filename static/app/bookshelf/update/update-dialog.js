<md-dialog  aria-label="book-label">
    <md-toolbar>
      <div class="md-toolbar-tools">
        <h2>Book</h2>
        <span flex></span>
        <md-button class="md-icon-button" ng-click="ctrl.cancel()">
          <ng-md-icon size="20" icon="clear" aria-label="Close dialog"></md-icon>
        </md-button>
      </div>
    </md-toolbar>
    <md-dialog-content class="md-dialog-content">
      <h2 class="md-title">Book</h2>
      <form name="myForm" class="container-fluid">
          <div layout="row" class="input-row layout-row">
            <md-input-container class="md-block">
                <label>Title</label>
                <input name="title" ng-model="book.title" md-auto-hide="false" ng-required="true" placeholder='ex. Origin'>
                <div ng-messages="myForm.title.$error">
                   <div ng-message="required">Title is required.</div>
                </div>
            </md-input-container>
          </div>
          <div layout="row" class="input-row layout-row">
            <md-input-container class="md-block">
                <label>Author</label>
                <input name="author" ng-model="book.author" md-auto-hide="false" ng-required="true" placeholder='ex. Dan Brown'>
                <div ng-messages="myForm.author.$error">
                   <div ng-message="required">Author is required.</div>
                </div>
            </md-input-container>
          </div>
          <div layout="row" class="input-row layout-row">
            <md-input-container>
              <label>Publish Date</label>
              <md-datepicker ng-model="book.publishdate" md-placeholder="Enter date" md-open-on-focus></md-datepicker>
            </md-input-container>
          </div>
          <div layout="row" class="input-row layout-row">
            <md-input-container class="md-block">
                <label>Description</label>
                <input name="desc" ng-model="book.description" md-auto-hide="false">
            </md-input-container>
          </div>
      </form>
    </md-dialog-content>
    <md-dialog-actions layout="row">
      <md-button class="md-raised md-primary" ng-disabled="myForm.$invalid" ng-click="ctrl.submit()">
        Update
      </md-button>
    </md-dialog-actions>
</md-dialog>

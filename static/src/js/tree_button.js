odoo.define('estate.tree_button', function (require) {
"use strict";
var ListController = require('web.ListController');
var ListView = require('web.ListView');
var viewRegistry = require('web.view_registry');
var TreeButton = ListController.extend({
   buttons_template: 'estate.property.buttons',
   events: _.extend({}, ListController.prototype.events, {
       'click .estate_property_type_action': '_OpenWizard',
   }),
   _OpenWizard: function () {
       var self = this;
        this.do_action({
           type: 'ir.actions.act_window',
           res_model: 'estate.property.type',
           name :'New Property Type',
           view_mode: 'form',
           view_type: 'form',
           views: [[false, 'form']],
           target: 'new',
           res_id: false,
       });
   }
});
var estate_property_view_tree = ListView.extend({
   config: _.extend({}, ListView.prototype.config, {
       Controller: TreeButton,
   }),
});
viewRegistry.add('button_in_tree', estate_property_view_tree);
});
# dhgh - Task1 Materiales Castelar: Warehouse shouldn't receive more than ordered quantity
[Link](https://www.odoo.com/web#id=3362270&cids=3&menu_id=4720&action=4665&active_id=3362248&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Functionally understand the functionality by playing with the UI
- [X] Figure out which models are required to be accessed/modified by hovering over fields (stock.picking.type and stock.move)in the UI 
- [X] Check which app the required models are in (stock)
- [X] Find a way to reach stock.picking.type from stock.move (via the picking_type_id field) with the models in the UI
- [X] Find the field to identify if the stock.picking.type record is a receipt (via the code field)
- [X] Implement a function with ondepends() decorator that checks the stock.picking.type.code for the particular stock.move record, compare quantity done with demand and raise User Error when needed

## Issues/Blocking Points

## Topics I need clarification on
      
## Interns who helped me

## Interns I helped

## Miscellaneous
- Considered using a computed field against the api.ondepends(), but api.ondepends() fits the situation here better
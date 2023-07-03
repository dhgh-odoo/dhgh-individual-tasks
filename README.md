# dhgh - Task2 LinkSource Pricing Update
[Link](https://www.odoo.com/web#id=3362285&cids=3&menu_id=4720&action=4665&active_id=3362248&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Functionally understand the issue by playing with the UI
- [X] Figure out which models are required to be accessed/modified by hovering over fields (sale.order and sale.order.line) in the UI 
- [X] Check which app the required models are in (sale)
- [X] Find the function which computes the unit price and override it (_get_display_price()) to prevent recomputing
- [X] Add a new button to recompute the unit prices and action (action_recompute_price_unit()) to implement the functionality
- [X] Use context to differentiate when the _get_display_price() function is being called (either from changing the quantity or by hitting the Recompute Prices button)

## Issues/Blocking Points

## Topics I need clarification on
      
## Interns who helped me

## Interns I helped

## Miscellaneous
- The approach used to prevent the unit price from recomputing is not optimal and given more time, I would explore a better option
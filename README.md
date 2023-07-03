# dhgh - Task3 Matrix Systems : Sequential Number for Barcode
[Link](https://www.odoo.com/web#id=3362252&cids=3&menu_id=4720&action=4665&active_id=3362248&model=project.task&view_type=form) to task

## Steps to complete the dev
- [X] Functionally understand the issue by playing with the UI
- [X] Figure out which models are required to be accessed/modified by hovering over fields (product.template) in the UI 
- [X] Check which app the required models are in (product)
- [x] Create a new field Product Groups in product.template
- [x] Add the product group field to the form view of product template
- [X] Create new entry in ir.sequence for the barcode
- [X] Find the function which computes the barcode and override it (_compute_barcode())

## Issues/Blocking Points

## Topics I need clarification on
      
## Interns who helped me

## Interns I helped

## Miscellaneous
- Made the barcode to be stored (store=True) to prevent updation of the sequence number for any change in the product group field
- Added sample groups to the product groups (for development prusposes)
# estate
# The Real Estate Advertisement module

Content:


## Creating The Employee

Log in as Administrator.

In the Settings App on the tab General Settings > Manage users or via menu Users And Companies > Users go to the Uses View and create a new user.

Fill in required Name and Email fields.

On the tab Access Rights choose
* Brokerage according the user's group: **Manager** or **Agent**
* Invoicing **Billing** or **leave empty** respectively
* Administaration **leave empty**

After saving the user date in **Action** > **Change Password** set the password.

## Views

There are three menus at the default view:
* Advertisements
  * [Properties](#properties-view)
* Settings
  * [Property Types](#property-type-view)
  * [Property Tags](#property-tag-view)

### Properties View

The default view is a **table** with main Property's attributes.

Information you can see:
* Title
* Property Type
* Salesman
* Postcode
* Tags
* Bedrooms
* Living Area
* Expected Price
* Selling Price
* Available From (by defult is hide)

It can be switched to **kanban** view with columns according to Property Type.

### Property Form View
([Up](#estate))

On the **Header** of the form view there are:
* Sold button
* Cancelled button
* Property Status statusbar (by default for Property without Offers is set to New)

The buttons become invisible after clicking on one of them. They change Property's Status according to their name. This action can not be undone!

If you try to Sold Property without Accepted Offer you will see the message:
* "The selling price is not set. You must accept an offer."

Property Status can be:
* New - there are no Offers
* Offer Received - when the first Offer is added
* Offer Accepted - when one of the Offers has been Accepted
* Sold - after clicking on the Sold button
* Cancelled - after clicking on the Cancelled button

The **top area** of the form view summarizes important information for the property, such as 
* Title (is required)
* Tags (represents as a bordered text with ability to set a colour. User can choose many tags)
* Type (one of the Property Types)
* Postcode
* Available From (by default is set to 3 months since the creation Property date)
* Expected Price (is required, must be grater than 0)
* Best Offer Price (is computed as a max Price from Property Offers)
* Selling Price (is set as a Price from the Accepted Property Offer, which was Sold)
* Active (by default is checked)

> If the **Real Estate Invoicing module** is installed after changing Property Status to Sold, the Invoice in the state Draft is created. 

The first tab **Description** contains information describing the property: 
* Description
* Bedrooms (by default is set to 2)
* Living Area (by default is set to 0)
* Garage (checkbox)
* Garden (by default is unchecked and the next two positions are invisible their value set to default)
  * Garden Orientation (by default is set to North)
  * Garden Area (by default is set to 0)
* Total Area (is computed as a summ of Living Area and Garden Area)

The second tab **Offers** lists the offers for the property. 
You can see here that potential buyers can make offers above or below the expected selling price. It is up to the seller to accept an offer.

Each line contains such information:
* Price (is required)
  * The offer price must be greater than 0
  * The offer price in new Offer must be higher than the Best Offer Price (max from existed Offer Prices)
  * The offer price must be greater than 90 percent of the expected price
* Buyer (is required)
* Validity(days) (by default is set to 7)
* Deadline (is related to Validity)
* Offer Status 
  * Acepted (check icon button)
  * Refused (X icon button)

For the Property can be created many Offers but Accepted can be **only one** Offer.

After the Offer is Accepted you **can not** create new or edit existed Offer.

If the Offer was Refused you **can not** edit this Offer.

The third tab **Other Info** tab with
  * Salesman (is required, by default is set user created the Property)
  * Buyer (is filled with the Buyer from Accepted Offer)

### Property Type Form View
([Up](#estate))

When creating a new Property Type or editing existed you can see
* **Properties** tab with a list of existed corresponded 
  * Properties (as in [Properties View](#properties-view)), 
  * their Expected Prices and 
  * Status
* **Description** and
* **Other Info** tab with
  * Salesman (is required, by default is set user created the Property Type)
  * Buyer (is required **need to be set!**)

On the top right you can see the widget with the number of the offers made for all existed properties of this type and can go to their list.

### Property Type View
([Up](#estate))

You can see it if you go to the menu Settings > Property Types.

It is a table with the option to re-order lines in it, making lines drag and droppable. It contains information:
* Property type
* number of the offers made for all existed properties of this type

For each Property Type you can see the [Property Type Form View](#property-type-form-view).

### Property Tag View
([Up](#estate))

You can see it if you go to the menu Settings > Property Tags. It is a list of existed tags.

## Security
([Up](#estate))

According to access rights and rules: 
* **Manager** employee 
  * can configure the system (manage available types and tags) as well as 
  * oversee every property in the pipeline. 
* **Agent** employee  
  * can manage the properties under their care, or properties which are not specifically under the care of any agent and 
  * not able update the property types or tags,
  * not able see the Settings menu
  * not able to see the properties exclusive to their colleagues.
* **Admin** user has manager rights.
* Employees who are **not** at least **Agents** will not see the real-estate application.

TODO Give nobody the right to delete properties.

TODO Manager is able to oversee every property in the pipeline. In multicompany mode - all properties in allowed companies.

The new user (remember to set a password), as the Agent should only see the real estate application, and possibly the Discuss (chat) application.

### User View

You can see the User information in the “Settings” app or click on the users name in the field **Salesman** on the[Properties View](#properties-view), [Property Form View](#property-form-view), and [Property Type View](#property-type-view)

Beside the standard information
* Name
* Email
* Company
* Phone
* Mobile

You can see the **Properties** tab like on the [Properties View](#properties-view) 

## Reports
([Up](#estate))

On the [Property Form View](#property-form-view) and on the [User View](#user-view) next to the Actions button you can see the Print button. It provides the ability to create documents to send to customers and to use internally.

On the Property Form View you can print a report that displays all offers for a property.

On the User View you can print all of the Properties that are visible in their form view.


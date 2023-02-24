# estate
# The Real Estate Advertisement module

## Views

There are three menus at the default view:
* Advertisements
  * Properties
* Settings
  * Property Types
  * Property Tags

The default view is a table with main Property's attributes.
It can be switched to kanban view with columns according to Property Type.

The **top area** of the form view summarizes important information for the property, such as 
* Title (is required)
* Tags (represents as a bordered text with ability to set a colour. User can choose many tags)
* Type (one of the Property Types)
* Postcode
* Date Aviability
* Expected Price (is required)
* Best Offer Price (is computed as a max Price from Property Offers)
* Selling Price (is set as a Price from the Accepted Property Offer, which was Sold)
* Active (by default is checked)

On the **Header** of the form view there are:
* Sold button
* Cancelled button
* Property Status statusbar (by default for Property without Offers is set to New)

Property Status can be:
* New - there are no Offers
* Offer Received - when the first Offer is added
* Offer Accepted - when one of the Offers has been Accepted
* Sold - after clicking on the Sold button
* Cancelled - after clicking on the Cancelled button

The buttons become invisible after clicking on one of them. They change Property's Status according to their name. This action can not be undone!

If the **Real Estate Invoicing module** is installed after changing Property Status to Sold, the Invoice in the state Draft is created. 


The first tab **Description** contains information describing the property: 
* Description
* Bedrooms (by default is set to 2)
* Living Area
* Garage (checkbox)
* Garden (if is checked the next two positions becomes visible, when is unchecked their value set to default)
  * Garden Orientation (by default is set to North)
  * Garden Area (by default is set to 0)
* Total Area (is computed as a summ of Living Area and Garden Area)

The second tab **Offers** lists the offers for the property. 
We can see here that potential buyers can make offers above or below the expected selling price. It is up to the seller to accept an offer.

There are messages showed according to the value of the prices:


## Security

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

## Reports



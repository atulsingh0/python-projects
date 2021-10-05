### Rotating Secret

Every Cloud has a Secret Implementation where we can store the sensitive information such as password, api-keys, ssh-keys, and many more.

In this problem, we will implement the similar logic but without using cloud (which will save some money :P).

- Secrets will be stored in a CSV file
- has 3 columns - Secret Id, Secret & Status (ACTIVE/INACTIVE)
- User will trigger the Program for a specific Secret ID
- Program will follow below steps -
  - If Secret ID does not exist, It will generate a Secret ID, Secret and Status as ACTIVE and Stored in the CSV file
  - If Secret ID exist, It will make the Status Inactive and Generate the another Secret and Stored the ID, Secret and Status as ACTIVE

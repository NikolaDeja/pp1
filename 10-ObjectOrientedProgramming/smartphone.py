import contact
import contact_list

c1=contact.Contact("John Brown","brown@onet.pl","555234000")
c2=contact.Contact("Anna May","am@o2.pl","232000199")
c3=contact.Contact("George Small","smallg@google.pl","222999100")
c4=contact.Contact("Paola Big","bigpaola@poczta.pl","100200300")

list=contact_list.Contact_list()

list.add(c1)
list.add(c2)
list.add(c3)
list.add(c4)

list.display()
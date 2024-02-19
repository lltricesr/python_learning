"""
    importing a module with a custom reference
    this module allows for manipulating xml files
"""
import xml.etree.ElementTree as ET

"""
    filename -> name of xml to be parsed
    ET:parse -> returns an ElementTree object of the read xml file
    tree:getroot -> returns and element of the top (first) element within the xml file
    xmlElements -> content within an XML file with enclosed tags <e></e> or <e/>
    root -> root element of the xml containing collection of all other elements (children)
    child -> element in root collection of indented elements
    element:attrib -> returns a dictionary of all the attributes contained in the element
    element:tag -> the element tag; tag has representation based on the type of xml document; represents type/name
"""
def parse_xml_et(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print ('Domains for: ' + root.attrib['name'])
    for child in root:
        print('\t' + child.attrib['name'], child.tag)

"""
    filename -> xml file that we are adding the element to; requires knowledge of the xml file
    el_tag -> tag of element that will be added as a new element
    attr -> attribute that we want to add to the element
    attr_val -> value of the attribute added to the element
    ET:parse -> read in the xml file and return the tree object
    tree:getroot -> return the root element of the xml file
    ET:Element -> create an element object based on el_tag; in this instance child of root
    child:attrib[attr] -> add the attribute of attr with the value of attr_val to the child element
    root:append -> append the child element to the root element collection of children elements
    tree:write -> write the output of the new xml tree including the added element back to the xml file
"""
def add_xml_element_et(filename, el_tag, attr, attr_val):
    tree = ET.parse(filename)
    root = tree.getroot()
    child = ET.Element(el_tag)
    child.attrib[attr] = attr_val
    root.append(child)
    tree.write(filename)

"""
    filename -> name of xml file
    el_tag -> name/tag of the element
    attr -> attribute to change
    oldval -> current value of the attribute
    newval -> new value that will be set to the attribute
    ET:parse -> read the xml file
    tree:root -> return the root/top element of the xml tree
    root:find(XPath) -> method will search the root element and return element for found element using the XPath; E.g. "root/domain[@name='Java']"
    child:attrib[attr] -> sets the attribute of the element
    tree.write() -> modifies xml file by writing updated tree back to xml file
"""
def change_xml_element_et(filename, el_tag, attr, oldval, newval):
    tree = ET.parse(filename)
    root = tree.getroot()
    child = root.find("./" + el_tag + "[@" + attr + "='" + oldval + "']")
    child.attrib[attr] = newval
    tree.write(filename)


"""
change_xml_element_et(
    './files_to_read/ef_author.xml',
    'domain',
    'name',
    'Java',
    'TypeScript'
)

add_xml_element_et(
    './files_to_read/ef_author.xml',
    'domain',
    'name',
    'Java'
)

parse_xml_et('./files_to_read/ef_author.xml')
"""
from docx import Document

# read_docx_content_in_order
# This function reads the content of a Word document in the order it appears in the document.
# It first loads the document from the specified file path.
# It then accesses the XML elements of the document body directly.
# For each element in the body, it checks if it is a paragraph or a table.
# If the element is a paragraph, it appends the text of the paragraph to the full_text list.
# If the element is a table, it iterates through the rows and cells of the table.
# For each cell, it concatenates the text of all the text elements in the cell.
# It then appends the concatenated cell texts for each row to the full_text list, separated by ' | '.
# Finally, it returns the combined text of the full_text list, with each element separated by a newline.
# 
# Parameters:
# file_path: The path to the Word document to read.
# 
# return: The combined text of the Word document.
def read_docx_content_in_order(file_path):  
    # Load the .docx file  
    doc = Document(file_path)  
    full_text = []  

    # Direct XML access (low-level, not recommended for complex operations)  
    body_elements = doc.element.body  # accessing the XML element  

    for elem in body_elements:  
        if elem.tag.endswith('p'):  # If the element is a paragraph  
            full_text.append(elem.text.strip())  
        elif elem.tag.endswith('tbl'):  # If the element is a table  
            # Iterate through rows and cells  
            for row in elem.findall('.//w:tr', doc.element.nsmap):  
                row_text = []  
                for cell in row.findall('.//w:tc', doc.element.nsmap):  
                    cell_text = ''.join(t.text for t in cell.findall('.//w:t', doc.element.nsmap))  
                    row_text.append(cell_text.strip())  
                full_text.append(' | '.join(row_text))  # Concatenate cell texts within a row  
  
    # Return the combined text  
    return '\n'.join(full_text)  
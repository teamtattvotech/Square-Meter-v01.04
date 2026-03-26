import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()

    # The footer social div closes with:
    #     </svg>
    #   </a>
    # </div>
    # Then there should be two more </div> tags before <!-- BOTTOM BAR -->
    
    # We will find <!-- BOTTOM BAR --> and check what is before it.
    parts = content.split("<!-- BOTTOM BAR -->")
    if len(parts) == 2:
        before = parts[0]
        # Check if right before <!-- BOTTOM BAR --> it has </div>
        # A simple check:
        # In index.html it has:
        # </div>
        # <!-- BOTTOM BAR -->
        # In contact.html it has:
        # </div>
        # 
        #   <!-- BOTTOM BAR -->
        
        # Let's count how many </div> we have since the start of footer
        
        # Simpler approach: replace the block with proper closing.
        # find: <div class="footer-social"> ... </div>
        # replace with: <div class="footer-social"> ... </div></div></div>
        
        pattern = re.compile(r'(<div class="footer-social">.*?</svg>\s*</a>\s*</div>)', re.DOTALL)
        content = pattern.sub(r'\1\n  </div>\n</div>', content)
        
        # But wait, index.html already has one </div> for footer-social but lacks footer-col and footer-container closing.
        # Wait, if we replace it, we might double-close if some files are correct.
        
        # Let's see if there are missing closures.
        # The structure is:
        # <footer class="site-footer">
        #   <div class="footer-container">
        #     ...
        #     <div class="footer-col">
        #       <h4>Contact</h4>
        #       <ul class="contact-list">...</ul>
        #       <div class="footer-social">...</div>
        # --> MISSING: </div> for col, </div> for container
        #   <!-- BOTTOM BAR -->
        
    with open(filepath, 'w') as f:
        f.write(content)


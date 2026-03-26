import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the footer-social div closing and add missing divs.
    target = '    </svg>\n  </a>\n</div>'
    
    if target in content:
        # Check what follows:
        idx = content.find(target) + len(target)
        after = content[idx:idx+100]
        print(f"File {filepath} has target. After:\n{after}\n---")
        
for f in glob.glob("*.html"):
    fix_file(f)


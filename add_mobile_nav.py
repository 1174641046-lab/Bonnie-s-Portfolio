import os

files = [
    ('project-01.html', '01', None, 'project-02.html'),
    ('project-02.html', '02', 'project-01.html', 'project-03.html'),
    ('project-03.html', '03', 'project-02.html', 'project-04.html'),
    ('project-04.html', '04', 'project-03.html', 'project-05.html'),
    ('project-05.html', '05', 'project-04.html', 'project-06.html'),
    ('project-06.html', '06', 'project-05.html', None),
]

css_mobile = '''\n/* 手机端底部项目导航 */
@media (max-width: 768px) {
  .mobile-project-nav {
    display: flex;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: rgba(10, 10, 10, 0.95);
    border-top: 1px solid rgba(126, 200, 80, 0.3);
    z-index: 1000;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    backdrop-filter: blur(8px);
  }
  .mobile-project-nav a {
    color: var(--green);
    text-decoration: none;
    font-size: 14px;
    letter-spacing: 0.1em;
    padding: 8px 16px;
    border: 1px solid rgba(126, 200, 80, 0.4);
    border-radius: 20px;
    transition: all 0.3s;
  }
  .mobile-project-nav a:hover,
  .mobile-project-nav a:active {
    background: rgba(126, 200, 80, 0.2);
  }
  .mobile-project-nav a.disabled {
    opacity: 0.3;
    pointer-events: none;
    border-color: rgba(126, 200, 80, 0.15);
  }
  .mobile-project-nav .nav-counter {
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.05em;
  }
  .project-footer {
    padding-bottom: 80px; /* 为底部导航栏留出空间 */
  }
}
'''

for filename, num, prev, next in files:
    filepath = filename
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add desktop CSS after .footer-copy rule
    content = content.replace(
        '.footer-copy {\n  font-size: 12px;\n  color: #444;\n  letter-spacing: 0.1em;\n}\n\n/* 侧箭头导航 */',
        '.footer-copy {\n  font-size: 12px;\n  color: #444;\n  letter-spacing: 0.1em;\n}\n\n.mobile-project-nav {\n  display: none;\n}\n\n/* 侧箭头导航 */'
    )
    
    # 2. Add mobile CSS before </style>
    content = content.replace(
        '}\n</style>\n</head>',
        '}' + css_mobile + '</style>\n</head>'
    )
    
    # 3. Add HTML nav between </main> and <footer>
    if prev is None:
        prev_html = '<span class="nav-prev disabled">← PREV</span>'
    else:
        prev_html = f'<a href="{prev}" class="nav-prev">← PREV</a>'
    
    if next is None:
        next_html = '<span class="nav-next disabled">NEXT →</span>'
    else:
        next_html = f'<a href="{next}" class="nav-next">NEXT →</a>'
    
    nav_html = f'''<nav class="mobile-project-nav">
  {prev_html}
  <span class="nav-counter">{num} / 06</span>
  {next_html}
</nav>'''
    
    content = content.replace(
        '</main>\n\n  <footer class="project-footer">',
        '</main>\n\n  ' + nav_html + '\n\n  <footer class="project-footer">'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Modified {filename}')

print('All files modified successfully.')

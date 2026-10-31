// ===== SIDEBAR MOBILE =====
document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.querySelector('.sidebar');
    const toggle = document.querySelector('.mobile-toggle');
    const overlay = document.querySelector('.sidebar-overlay');

    if (toggle && sidebar) {
        toggle.addEventListener('click', function () {
            sidebar.classList.toggle('open');
            if (overlay) overlay.classList.toggle('active');
        });

        if (overlay) {
            overlay.addEventListener('click', function () {
                sidebar.classList.remove('open');
                overlay.classList.remove('active');
            });
        }

        // Fechar ao clicar em link (mobile)
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function () {
                if (window.innerWidth <= 1024) {
                    sidebar.classList.remove('open');
                    if (overlay) overlay.classList.remove('active');
                }
            });
        });
    }

    // ===== BOTÃO VOLTAR AO TOPO =====
    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ===== MARCAR LINK ATIVO NA SIDEBAR =====
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.sidebar-nav a').forEach(link => {
        const href = link.getAttribute('href');
        if (href && (href === currentPath || href.endsWith(currentPath))) {
            link.classList.add('active');
        }
    });

    // ===== WRAPPER PARA TABELAS (responsivo) =====
    document.querySelectorAll('.content-wrapper table').forEach(table => {
        if (!table.parentElement.classList.contains('table-wrapper')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'table-wrapper';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });

    // ===== DETECTAR LINGUAGEM EM <pre><code> =====
    document.querySelectorAll('.content-wrapper pre').forEach(pre => {
        const code = pre.querySelector('code');
        if (code) {
            const cls = code.className || '';
            const match = cls.match(/language-(\w+)/);
            if (match) {
                pre.setAttribute('data-lang', match[1]);
            } else {
                // Tenta inferir pelo conteúdo
                const text = code.textContent.trim();
                if (/^(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP)\b/i.test(text)) {
                    pre.setAttribute('data-lang', 'sql');
                } else if (/^(def |import |from |class )/.test(text)) {
                    pre.setAttribute('data-lang', 'python');
                } else if (/[{};]\s*$/.test(text) && /function|const|let|var/.test(text)) {
                    pre.setAttribute('data-lang', 'js');
                } else if (/^#include|int main/.test(text)) {
                    pre.setAttribute('data-lang', 'c');
                }
            }
        }
    });

    // ===== SCROLL SUAVE PARA ÂNCORAS =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});
// 指定した拡張子のファイルのみを許可するスクリプト
// 作成者 Naoki

(function() {
    'use strict';
    window.addEventListener('load', function() {
        let forms = document.getElementsByClassName('needs-validation');
        let validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();
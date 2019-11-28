
    console.log( "ready!" );
    let modal = document.getElementById('Modal');
    // let btn = document.getElementById("callbackBtn");
    let span = document.getElementsByClassName("close")[0];
    // btn.onclick = function() {
    //   modal.style.display = "block";
    // }
    span.onclick = function() {
      modal.style.display = "none";
    }
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }



    $('.carousel').slick({
        arrows: true,
        autoplay: false,
        autoplaySpeed: 2000,
        dots: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerPadding:'170px',
        prevArrow: $('.prev'),
        nextArrow: $('.next'),
        centerMode: false,





    });
    $('.carousel1').slick({
        arrows: true,
        autoplay: false,
        autoplaySpeed: 3000,
        dots: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerPadding:'50px',
        prevArrow: $('.prev1'),
        nextArrow: $('.next1'),
        centerMode: false,


    });

    jQuery(function($){
        $("#home-client-phone").mask("+7 (999) 999-99-99");
    });
     jQuery(function($){
        $("#modal-client-phone").mask("+7 (999) 999-99-99");
    });

     function showmodal(type) {
         let modalBtn = $('#modal-button')
         let modalHeader = $('#modal-header')
         let modalText = $('#modal-text')
        if (type === 'callback'){
            modalHeader.html('Свяжитесь с нами!')
             modalText.html('Заполните оба поля и нажмите на кнопку, после чего наш оператор перезвонит вам')
            modalBtn.html('Заказать звонок')
            modal.style.display = "block";
            ym(54048193, 'reachGoal', 'sdelat_zakaz1');
        }
         if (type === 'order'){
             modalHeader.html('Свяжитесь с нами!')
             modalText.html('Заполните оба поля и нажмите на кнопку, после чего наш оператор перезвонит вам')
             modalBtn.html('Сделать заказ')
             modal.style.display = "block";
             ym(54048193, 'reachGoal', 'sdelat_zakaz1');
        }
         if (type === 'dizain'){
             modalHeader.html('Cпециально для вас:')
             modalText.html('- Бонусная программа;<br>\n' +
                 '            - Каталоги по всему ассортименту;<br>\n' +
                 '            - Размещение Вашего портфолио на нашем сайте;<br>\n' +
                 '            - Предоставление клиентов для Ваших проектов;<br>\n' +
                 '            - Широкий ассортимент 3Д панелей.')
             modalBtn.html('Заказать звонок')
             modal.style.display = "block";
        }
         if (type === 'diler'){
             modalHeader.html('Cпециально для вас:')
             modalText.html(' - Дилерская скидка без привязки к объемам;<br>\n' +
                 '            - Закрепление территории;<br>\n' +
                 '            - Бесплатные выставочные образцы и каталоги;<br>\n' +
                 '            - Размещение информации о Вас на нашем сайте;<br>\n' +
                 '            - Рекламная поддержка;<br>\n' +
                 '            - Информационная поддержка.')
             modalBtn.html('Заказать звонок')
             modal.style.display = "block";
        }
         if (type === 'catalog'){
            modalHeader.html('Полный каталог продукции бесплатно!')
             modalText.html('Заполните оба поля и нажмите на кнопку, после чего наш оператор перезвонит вам')
            modalBtn.html('Получить каталог')
            modal.style.display = "block";
        }


    }


function homeCallback(e) {
    e.preventDefault();
    client_name = document.getElementById("home-client-name").value;
    client_phone = document.getElementById("home-client-phone").value;
    console.log('send form');

	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'call_form.php', true);
	xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xhr.onload = function () {
		btn = document.getElementById("home-submit-btn")
		btn.innerHTML = 'Отправлено'
		btn.disabled = true
		console.log(this.responseText);
		};
	xhr.send('client_name='+client_name+'&client_phone='+client_phone);
}



function modalCallback(e) {
    e.preventDefault();
    client_name = document.getElementById("modal-client-name").value;
    client_phone = document.getElementById("modal-client-phone").value;
    console.log('send modal form');
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'call_form.php', true);
	xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xhr.onload = function () {

		console.log(this.responseText);
		btn = document.getElementById("modal-button")
		btn.innerHTML = 'Отправлено'
		btn.disabled = true
		};
	xhr.send('client_name='+client_name+'&client_phone='+client_phone);

}

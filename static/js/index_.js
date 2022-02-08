var slideIndex = 0;
        showSlides();
        
        function showSlides() {
          var i;
          var slides = document.getElementsByClassName("mySlides");
          var dots = document.getElementsByClassName("dot");
          for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
          }
          slideIndex++;
          if (slideIndex > slides.length) {slideIndex = 1}    
          for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
          }
          slides[slideIndex-1].style.display = "block";  
          dots[slideIndex-1].className += " active";
          setTimeout(showSlides, 10000); // Change image every 2 seconds

          
        }




function change_to_AR(){

  var dec = {
    home:['home', 'الرئسية'],
    members:['members', 'الاعضاء'],
    about:['about', 'حولنا'],
    help_:['help', 'المساعدة'],
    
    //anther thing

    man : ['MAN', "رجال"],
    info_man : ['MAN', "رجال"],
    goto: ['GO TO', 'اذهب'],

    weman : ['WEMAN', "نساء"],
    info_man : ['MAN', "نساء"],
    Goto: ['GO TO', 'اذهب'],

    New : ['NEW', "اضافة جديد"],
    info_man : ['', ''],
    add_new: ['ADD', 'اضافه'],


    }
    var sel = document.getElementById('select_');
    console.log(sel.value);


  if (sel.value == 'AR'){

    document.getElementById('right_').style.direction='rtl'


    document.getElementById('home').innerHTML = dec.home[1];
    document.getElementById('members').innerHTML = dec.members[1] ;
    document.getElementById('about').innerHTML = dec.about[1] ;
    document.getElementById('help').innerHTML = dec.help_[1] ;

    //ather
    document.getElementById('man').innerHTML = dec.man[1];
    //document.getElementById('Goto').innerHTML = dec.goto[1];
    document.getElementById('Goto').innerHTML = dec.Goto[1];


    document.getElementById('add_new').innerHTML = dec.New[1];
    //document.getElementById('add_new').innerHTML = dec.add_new[1];
    document.getElementById('add_newd').innerHTML = dec.add_new[1];



    document.getElementById('weman').innerHTML = dec.weman[1];
    //document.getElementById('add_new').innerHTML = dec.add_new[1];
    document.getElementById('Goto_').innerHTML = dec.Goto[1];


    



  }
  else{


  
    document.getElementById('right_').style.direction='ltr'


    document.getElementById('home').innerHTML = dec.home[0];
    document.getElementById('members').innerHTML = dec.members[0] ;
    document.getElementById('about').innerHTML = dec.about[0] ;
    document.getElementById('help').innerHTML = dec.help_[0] ;

    //ather
    document.getElementById('man').innerHTML = dec.man[0];
    //document.getElementById('Goto').innerHTML = dec.goto[0];
    document.getElementById('Goto').innerHTML = dec.Goto[0];


    document.getElementById('add_new').innerHTML = dec.New[0];
    //document.getElementById('add_new').innerHTML = dec.add_new[0];
    document.getElementById('add_newd').innerHTML = dec.add_new[0];



    document.getElementById('weman').innerHTML = dec.weman[0];
    //document.getElementById('add_new').innerHTML = dec.add_new[0];
    document.getElementById('Goto_').innerHTML = dec.Goto[0];


    

  }

  console.log('its done')
  console.log(dec.home[1]);




}
// student_list.html

function student_list(params) {
    let student_list_search = document.querySelector('.student_list #DataTables_Table_0_wrapper #search_input')
    let student_list_search_div= document.querySelector('.student_list .search_sec')
    let student_list_form= document.querySelector('.student_list .search_sec form')
    
    student_list_search_div.style.display = 'none'
    
    let cond = true
    
    student_list_search.addEventListener('click',function(){
        student_list_search_div.style.display = 'flex'
    })
    
    student_list_form.addEventListener('click',function(){
        if (cond) {
            
            student_list_search_div.style.display = 'flex'
            cond=false
       
    
        }
    })
    
    student_list_search_div.addEventListener('click',function(e){
        
        if (cond) {
            
            student_list_search_div.style.display = 'none'
            
            
    
        }
        cond=true
    })

var modal = document.querySelectorAll(".modals");

// Get the button that opens the modal
var btn = document.querySelectorAll(".myBtn");

// Get the <span> element that closes the modal
var span = document.querySelectorAll(".close");

// When the user clicks the button, open the modal 

for (const i in btn) {
  btn[i].onclick = function() {

    modal[i].style.display = "block";
    
  }
}

// When the user clicks on <span> (x), close the modal
for (const i in span) {
  
  span[i].onclick = function() {
   
    modal[i].style.display = "none";
  }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
for (const i in modal) {
    if (event.target == modal[i]) {
      modal[i].style.display = "none";
      
    }
  }
}
}

student_list()

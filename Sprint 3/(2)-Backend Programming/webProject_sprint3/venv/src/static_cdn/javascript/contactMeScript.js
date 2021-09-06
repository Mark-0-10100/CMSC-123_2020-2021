/*This block of code corresponds to the animation 
when the search bar when page is opened

    "gsap.from(a,{b})"   
    - a function from gsap
    - animation that is targeted to class="searchBar-container"

    "y: 1000" ".from"
    - the division initially comes "from" 1000 units below away

    "ease: Power4.easeOut"
    - sets the animation flow

----------------------------------------------------------------------*/
gsap.from(".contactMeContainer",{
    opacity: 0,
    y: 1000,
    ease: Power4.easeOut,
    duration: 2
});
//----------------------------------------------------------------------


/*Form Validation JavaScript
•This block of code contains the script for validating the forms
•More codes will be added in Sprint3, for the database
*/

function validateForm() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;
    let validationErrorText = "";

    if (name == "" ) {
        validationErrorText = "Please enter a name";
    }
    else if (email == "") {
        validationErrorText = "Please enter an email address";
    }
    else if (message == "") {
        validationErrorText = "Please enter an email address";
    }
    else{
         alert("Hi " + name + "! Thank you for submitting a message!" )
    }
    document.getElementById("validationError").innerHTML = validationErrorText;
}
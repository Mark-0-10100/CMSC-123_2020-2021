/*This block of code corresponds to the animation 
when the search bar when page is opened

    "gsap.from(a,{b})"   
    - a function from gsap
    - animation that is targeted to class="searchBar-container"

    "x: -1000" ".from"
    - the division initially comes "from" the left -1000 units away

    "ease: Power4.easeOut"
    - sets the animation flow

----------------------------------------------------------------------*/
gsap.from(".searchBar-container",{
    x: -1000,
    ease: Power4.easeOut,
    duration: 2}
);
//----------------------------------------------------------------------



/*This block of code corresponds to the animation 
when the blog page is opened

    "gsap.from(a,{b})"   
    - a function from gsap
    - animation that is targeted to class="searchBar-container"

    "x: -1000" ".from"
    - the division initially comes "from" the left -1000 units away

    "ease: Power4.easeOut"
    - sets the animation flow*/

gsap.from(".searchBar-container",{
    x: -1000,
    ease: Power4.easeOut,
    duration: 2}
);
//----------------------------------------------------------------------

gsap.from(".divisionTitle",{ // ".divisionTitle" is being animated
    opacity: 0,
    y: -100, //the division initially comes "from" the top -100 units away vertically
    ease: Power4.easeOut, //the animation flow
    duration: 2
});
//----------------------------------------------------------------------

//Blogs container animation
gsap.from(".blog-container",{
    x: -2000,
    ease: Power4.easeOut,
    stagger: .5, //Allows elements in a class to animate one "after" the other
    duration: 2}
);


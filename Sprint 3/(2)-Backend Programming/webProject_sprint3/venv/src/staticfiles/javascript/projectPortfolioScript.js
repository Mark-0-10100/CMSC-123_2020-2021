gsap.registerPlugin(ScrollTrigger); // registers/import plugin when certain part of page is scrolled through.

let t1 = gsap.timeline(); //creates a separate timeline for the other animations in this page

t1.from(".softwareProj", { //".softwareProj" is being animated
    delay: .5,
    stagger: 1, //allows elements to animate one after the other
    duration: 2,
    x: 3000, //the division initially comes "from" the left 3000 units away horizontally
    ease: Power4.easeOut //the animation flow
})

gsap.from(".divisionTitle",{ //uses the main gsap timline; ".divisionTitle" is being animated
    opacity: 0,
    y: -100, //the division initially comes "from" the top -100 units away vertically
    ease: Power4.easeOut, //the animation flow
    duration: 2
});

gsap.from(".artprojContainer", { //".artprojContainer" is being animated
    scrollTrigger: { //animation only triggers when this part of the page is scrolled through
        trigger: ".artprojContainer",
        start: "top bottom",
    },
    duration: 1, //animation for the image tiles
    opacity: 0, //goes from being invisible to visible
    scale: 0.5, //goes from smaller to bigger
    delay: 0.5, 
    stagger: 0.5, //allows image tiles to animate one after the other
    ease: "elastic", 
    force3D: true 
})

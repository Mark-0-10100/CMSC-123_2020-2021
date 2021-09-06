/*All of the codes here corresponds to the animation 
when the search bar when page is opened*/

//List of words to be looped through
let words = ["a CompSci Student.", 
  "an amateur Web Developer.",      
  "an amateur Artist.", 
  "an amateur Researcher."]

/*creates a timeline about my occupation
    "gsap.timeline({})"
    -creates a timeline for the animations

    "({repeat: -1})"
    -repeats infinitely
*/
let occupTimeLine = gsap.timeline({repeat: -1}).pause()

//creates another TimeLine for the greetings animation
let greetingsTimeLine = gsap.timeline()

// animates the greetings
// this block of code is within the "greetingsTimeLine" ----------------/
greetingsTimeLine.from('.greet', {
  duration:1,          
  x:"-1000px",        //the division initially comes "from" the left -1000 units away
  ease: "power3.out"} //the animation flow
)

.from('.occupation', {
  delay: 0, 
  x:"-1000px",        //comes "from" the left -1000 units away
  ease: "power3.out", //the animation flow
  onComplete: () => occupTimeLine.play()} //plays the other timeline for the occupation
)
//----------------------------------------------------------------------/


// this block of code loops through the list of words for my occupation ----------/
words.forEach(x => {
  let tl = gsap.timeline({repeat: 1, //a timeLine within this loop
    yoyo: true, //animation flow
    repeatDelay:1}) //delay for each repeat
  tl.to('.occupation', {duration: 1, text: x})
  occupTimeLine.add(tl) //adds the words in class=".occupation" 
})

//---------------------------------------------------------------------------------/
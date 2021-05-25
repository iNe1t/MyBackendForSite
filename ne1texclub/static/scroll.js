var controller = new ScrollMagic.Controller();

new ScrollMagic.Scene({triggerElement: "#main_trigger"})
							// trigger animation by adding a css class
							.setClassToggle("#header", "scroll_change")
							.addTo(controller);
new ScrollMagic.Scene({triggerElement: "#main_trigger"})
							// trigger animation by adding a css class
                            .setClassToggle("#button", "dark_text")
							.addTo(controller);
new ScrollMagic.Scene({triggerElement: "#main_trigger"})
							// trigger animation by adding a css class
                            .setClassToggle("#ul-header", "dark_text")
							.addTo(controller);
new ScrollMagic.Scene({triggerElement: "#main_trigger"})
							// trigger animation by adding a css class
                            .setClassToggle("#menu1", "sidescroll_change")
							.addTo(controller);
new ScrollMagic.Scene({triggerElement: "#main_trigger"})
							// trigger animation by adding a css class
                            .setClassToggle("#buttonz", "dark_text")
							.addTo(controller);

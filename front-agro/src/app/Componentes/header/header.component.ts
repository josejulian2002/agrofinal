import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  returnnav(){
    document.getElementById("navmenu").style.transform = "translate(-15em,-6em)"
  }
  shownav(){
    document.getElementById("navmenu").style.transform = "translate(0em,-6em)"
  }

}

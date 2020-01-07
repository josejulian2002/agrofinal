import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header-usuario',
  templateUrl: './header-usuario.component.html',
  styleUrls: ['./header-usuario.component.css']
})
export class HeaderUsuarioComponent implements OnInit {

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

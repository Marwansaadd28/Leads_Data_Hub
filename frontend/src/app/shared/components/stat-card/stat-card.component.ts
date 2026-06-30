import { Component, Input } from '@angular/core';

import { CardModule } from 'primeng/card';

@Component({
  selector: 'app-stat-card',
  standalone: true,
  imports: [CardModule],
  templateUrl: './stat-card.component.html',
  styleUrl: './stat-card.component.css'
})
export class StatCardComponent {

  @Input() title = '';

  @Input() value = 0;

  @Input() icon = '';

}

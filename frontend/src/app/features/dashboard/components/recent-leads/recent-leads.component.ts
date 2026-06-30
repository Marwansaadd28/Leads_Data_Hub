import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

import { TableModule } from 'primeng/table';
import { TagModule } from 'primeng/tag';
import { ButtonModule } from 'primeng/button';

import { RecentLead } from '../../../../core/models/dashboard.model';

@Component({
  selector: 'app-recent-leads',
  standalone: true,
  imports: [
    CommonModule,
    TableModule,
    TagModule,
    ButtonModule
  ],
  templateUrl: './recent-leads.component.html',
  styleUrl: './recent-leads.component.css'
})
export class RecentLeadsComponent {

  @Input() leads: RecentLead[] = [];

  getSeverity(status: string) {
    switch (status.toLowerCase()) {
      case 'new':
        return 'success';
      case 'contacted':
        return 'info';
      case 'qualified':
        return 'warning';
      case 'lost':
        return 'danger';
      default:
        return 'secondary';
    }
  }
}
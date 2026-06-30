import { Component, OnInit, inject } from '@angular/core';

import { DashboardService } from '../../core/services/dashboard.service';
import { DashboardResponse } from '../../core/models/dashboard.model';

import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { StatCardComponent } from '../../shared/components/stat-card/stat-card.component';



@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    StatCardComponent,
    ProgressSpinnerModule
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  private dashboardService = inject(DashboardService);

  dashboard?: DashboardResponse;

  ngOnInit(): void {

    this.loadDashboard();

  }

  loadDashboard(): void {

    this.dashboardService.getDashboard().subscribe({

      next: (response) => {

        console.log(response);

        this.dashboard = response;

      },

      error: (error) => {

        console.error(error);

      }

    });

  }

}
import { Component, OnInit, inject } from '@angular/core';

import { CardModule } from 'primeng/card';
import { ChartModule } from 'primeng/chart';

import { DashboardService } from '../../core/services/dashboard.service';
import { DashboardResponse } from '../../core/models/dashboard.model';
import { RecentLeadsComponent } from './components/recent-leads/recent-leads.component';
import { StatCardComponent } from '../../shared/components/stat-card/stat-card.component';
import { StatusChartComponent } from './components/status-chart/status-chart.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [

    StatCardComponent,

    CardModule,

    ChartModule,

    RecentLeadsComponent,

    StatusChartComponent
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  private dashboardService = inject(DashboardService);

  dashboard?: DashboardResponse;

  sourceChartData: any;

  sourceChartOptions: any;

  ngOnInit(): void {
    this.loadDashboard();
  }

  loadDashboard(): void {

    this.dashboardService.getDashboard().subscribe({

      next: (response) => {

        console.log(response);

        this.dashboard = response;

        this.sourceChartData = {
          labels: response.leads_by_source.map(item => item.name),
          datasets: [
            {
              data: response.leads_by_source.map(item => item.count)
            }
          ]
        };

        this.sourceChartOptions = {
          plugins: {
            legend: {
              position: 'bottom'
            }
          },
          responsive: true,
          maintainAspectRatio: false
        };

      },

      error: (error) => {

        console.error(error);

      }

    });

  }

}
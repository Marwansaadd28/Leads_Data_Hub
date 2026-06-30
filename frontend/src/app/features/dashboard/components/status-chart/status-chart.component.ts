import { Component, Input, OnChanges } from '@angular/core';

import { CardModule } from 'primeng/card';
import { ChartModule } from 'primeng/chart';

import { DashboardItem } from '../../../../core/models/dashboard.model';

@Component({
  selector: 'app-status-chart',
  standalone: true,
  imports: [
    CardModule,
    ChartModule
  ],
  templateUrl: './status-chart.component.html',
  styleUrl: './status-chart.component.css'
})
export class StatusChartComponent implements OnChanges {

  @Input() data: DashboardItem[] = [];

  chartData: any;

  chartOptions: any;

  ngOnChanges(): void {

    this.chartData = {

      labels: this.data.map(item => item.name),

      datasets: [

        {

          label: 'Leads',

          data: this.data.map(item => item.count),

          borderRadius: 8

        }

      ]

    };

    this.chartOptions = {

      responsive: true,

      maintainAspectRatio: false,

      plugins: {

        legend: {

          display: false

        }

      }

    };

  }

}
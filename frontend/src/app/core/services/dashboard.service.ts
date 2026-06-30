import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { DashboardResponse } from '../models/dashboard.model';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private http = inject(HttpClient);

  private readonly apiUrl =
    'http://127.0.0.1:8000/api/leads/dashboard/';

  getDashboard(): Observable<DashboardResponse> {

    return this.http.get<DashboardResponse>(
      this.apiUrl
    );

  }

}
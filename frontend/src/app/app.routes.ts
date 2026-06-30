import { Routes } from '@angular/router';

import { DashboardComponent } from './features/dashboard/dashboard.component';
import { LeadsComponent } from './features/leads/leads.component';
import { LeadDetailsComponent } from './features/lead-details/lead-details.component';
import { LeadFormComponent } from './features/lead-form/lead-form.component';

export const routes: Routes = [

  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full'
  },

  {
    path: 'dashboard',
    component: DashboardComponent
  },

  {
    path: 'leads',
    component: LeadsComponent
  },

  {
    path: 'leads/new',
    component: LeadFormComponent
  },

  {
    path: 'leads/:id',
    component: LeadDetailsComponent
  },

  {
    path: 'leads/:id/edit',
    component: LeadFormComponent
  },

  {
    path: '**',
    redirectTo: 'dashboard'
  }

];
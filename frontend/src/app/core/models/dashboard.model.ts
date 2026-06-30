export interface DashboardSummary {

    total_leads: number;

    total_sources: number;

    total_statuses: number;

}

export interface DashboardItem {

    name: string;

    count: number;

}

export interface RecentLead {

    lead_id: number;

    name: string;

    email: string;

    source: string;

    status: string;

    created_at: string;

}

export interface DashboardResponse {

    summary: DashboardSummary;

    leads_by_source: DashboardItem[];

    leads_by_status: DashboardItem[];

    recent_leads: RecentLead[];

}
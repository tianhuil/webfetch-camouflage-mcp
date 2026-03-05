<style>
@media (max-width: 800px) {
  .comparison-table td {
    display: block !important;
    width: 100% !important;
  }
}
</style>

<p style="font-size: 20px; font-weight: 600;">Give your AI coding assistant reliable access to web pages that block standard fetch.</p>

<table class="comparison-table" style="border-collapse: collapse; width: 100%; margin: 20px 0; max-width: 800px">
  <tr>
    <td style="width: 50%; padding: 15px; vertical-align: top;">
      <div style="overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; background: #fff; box-shadow: 0 0 60px -8px rgba(239, 68, 68, 0.45); transition: transform 0.2s;">
        <div style="position: relative; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #e2e8f0; background: #f8fafc; padding: 10px 16px;">
          <div style="position: absolute; left: 16px; display: flex; gap: 6px;">
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #ff5f57;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #febc2e;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #28c840;"></span>
          </div>
          <span style="font-size: 11px; color: #64748b;">Standard fetch</span>
        </div>
        <div style="padding: 16px;">
          <div style="display: flex; flex-direction: column; gap: 12px; font-family: monospace; font-size: 12px;">
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #f1f5f9; color: #64748b;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              </div>
              <p style="color: #64748b;">Read http://docs.example.com</p>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #fef2f2; color: #dc2626;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>
              </div>
              <p style="color: #991b1b;">Error: 404 - Blocked by bot detection</p>
            </div>
          </div>
        </div>
      </div>
    </td>
    <td style="width: 50%; padding: 15px; vertical-align: top;">
      <div style="overflow: hidden; border-radius: 12px; border: 1px solid #e2e8f0; background: #fff; box-shadow: 0 0 60px -8px rgba(34, 197, 94, 0.45); transition: transform 0.2s;">
        <div style="position: relative; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #e2e8f0; background: #f8fafc; padding: 10px 16px;">
          <div style="position: absolute; left: 16px; display: flex; gap: 6px;">
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #ff5f57;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #febc2e;"></span>
            <span style="height: 12px; width: 12px; border-radius: 50%; background: #28c840;"></span>
          </div>
          <span style="font-size: 11px; color: #64748b;">Webfetch Camouflage</span>
        </div>
        <div style="padding: 16px;">
          <div style="display: flex; flex-direction: column; gap: 12px; font-family: monospace; font-size: 12px;">
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #f1f5f9; color: #64748b;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
              </div>
              <p style="color: #64748b;">Read http://docs.example.com</p>
            </div>
            <div style="display: flex; align-items: flex-start; gap: 8px;">
              <div style="display: flex; height: 20px; width: 20px; align-items: center; justify-content: center; border-radius: 50%; background: #dcfce7; color: #16a34a;">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 12px; height: 12px;"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>
              </div>
              <p style="color: #166534;">Success: 200 OK - Page fetched!</p>
            </div>
          </div>
        </div>
      </div>
    </td>
  </tr>
</table>

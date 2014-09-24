/**
 * This software was developed and / or modified by Raytheon Company,
 * pursuant to Contract DG133W-05-CQ-1067 with the US Government.
 * 
 * U.S. EXPORT CONTROLLED TECHNICAL DATA
 * This software product contains export-restricted data whose
 * export/transfer/disclosure is restricted by U.S. law. Dissemination
 * to non-U.S. persons whether in the United States or abroad requires
 * an export license or other authorization.
 * 
 * Contractor Name:        Raytheon Company
 * Contractor Address:     6825 Pine Street, Suite 340
 *                         Mail Stop B8
 *                         Omaha, NE 68106
 *                         402.291.0100
 * 
 * See the AWIPS II Master Rights File ("Master Rights File.pdf") for
 * further licensing information.
 **/
package com.raytheon.uf.viz.monitor.safeseas.ui.dialogs;

import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Shell;

import com.raytheon.uf.common.monitor.config.FSSObsMonitorConfigurationManager;
import com.raytheon.uf.common.monitor.config.FSSObsMonitorConfigurationManager.MonName;
import com.raytheon.uf.common.monitor.data.CommonConfig;
import com.raytheon.uf.common.monitor.data.CommonConfig.AppName;
import com.raytheon.uf.common.monitor.data.ObConst.DataUsageKey;
import com.raytheon.uf.viz.monitor.safeseas.SafeSeasMonitor;
import com.raytheon.uf.viz.monitor.safeseas.threshold.SSThresholdMgr;
import com.raytheon.uf.viz.monitor.ui.dialogs.MonitoringAreaConfigDlg;

/**
 * SAFESEAS area configuration dialog.
 * 
 * <pre>
 * 
 * SOFTWARE HISTORY
 * Date         Ticket#    Engineer    Description
 * ------------ ---------- ----------- --------------------------
 * Jan  5, 2010            mpduff      Initial creation
 * Nov 27, 2012 1351       skorolev    Changes for non-blocking dialog.
 * Jan 29, 2014 2757       skorolev    Changed OK button handler.
 * Apr 23, 2014 3054       skorolev    Fixed issue with removing a new station from list.
 * Apr 28, 2014 3086       skorolev    Updated getConfigManager.
 * Sep 15, 2014 2757       skorolev    Removed extra dialog.
 * 
 * </pre>
 * 
 * @author mpduff
 * @version 1.0
 */

public class SSMonitoringAreaConfigDlg extends MonitoringAreaConfigDlg {

    /** Configuration manager for SAFESEAS monitor. */
    private FSSObsMonitorConfigurationManager ssConfigMgr;

    /**
     * Constructor
     * 
     * @param parent
     * @param title
     */
    public SSMonitoringAreaConfigDlg(Shell parent, String title) {
        super(parent, title, AppName.SAFESEAS);
    }

    /*
     * (non-Javadoc)
     * 
     * @see com.raytheon.uf.viz.monitor.ui.dialogs.MonitoringAreaConfigDlg#
     * handleOkBtnSelection()
     */
    @Override
    protected void handleOkBtnSelection() {
        // Check for changes in the data
        if (dataIsChanged()) {
            int choice = showMessage(shell, SWT.OK | SWT.CANCEL,
                    "SAFESEAS Monitor Confirm Changes",
                    "Want to update the SAFESEAS setup files?");
            if (choice == SWT.OK) {
                // Save the config xml file
                getValues();
                resetStatus();
                ssConfigMgr.saveConfigXml();
                /**
                 * DR#11279: re-initialize threshold manager and the monitor
                 * using new monitor area configuration
                 */
                SSThresholdMgr.reInitialize();
                SafeSeasMonitor.reInitialize();
                if ((!ssConfigMgr.getAddedZones().isEmpty())
                        || (!ssConfigMgr.getAddedStations().isEmpty())) {
                    if (editDialog() == SWT.YES) {
                        SSDispMonThreshDlg ssMonitorDlg = new SSDispMonThreshDlg(
                                shell, CommonConfig.AppName.SAFESEAS,
                                DataUsageKey.MONITOR);
                        ssMonitorDlg.open();
                    }
                    ssConfigMgr.getAddedZones().clear();
                    ssConfigMgr.getAddedStations().clear();
                }
            }
        } 
    }

    /*
     * (non-Javadoc)
     * 
     * @see
     * com.raytheon.uf.viz.monitor.ui.dialogs.MonitoringAreaConfigDlg#getInstance
     * ()
     */
    public FSSObsMonitorConfigurationManager getInstance() {
        if (ssConfigMgr == null) {
            ssConfigMgr = new FSSObsMonitorConfigurationManager(currentSite,
                    MonName.ss.name());
        }
        return (FSSObsMonitorConfigurationManager) ssConfigMgr;
    }

    /*
     * (non-Javadoc)
     * 
     * @see
     * com.raytheon.uf.viz.monitor.ui.dialogs.MonitoringAreaConfigDlg#disposed()
     */
    @Override
    protected void disposed() {
        ssConfigMgr = null;
    }
}

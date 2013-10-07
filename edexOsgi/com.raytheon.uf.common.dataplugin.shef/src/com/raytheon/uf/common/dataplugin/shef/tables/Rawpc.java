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
package com.raytheon.uf.common.dataplugin.shef.tables;

// default package
// Generated Oct 17, 2008 2:22:17 PM by Hibernate Tools 3.2.2.GA

import java.util.Date;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Transient;

/**
 * Rawpc generated by hbm2java
 * 
 * 
 * <pre>
 * 
 * SOFTWARE HISTORY
 * Date         Ticket#    Engineer    Description
 * ------------ ---------- ----------- --------------------------
 * Oct 17, 2008                        Initial generation by hbm2java
 * Aug 19, 2011      10672     jkorman Move refactor to new project
 * Oct 07, 2013       2361     njensen Removed XML annotations
 * 
 * </pre>
 * 
 * @author jkorman
 * @version 1.1
 */
@Entity
@Table(name = "rawpc")
@com.raytheon.uf.common.serialization.annotations.DynamicSerialize
public class Rawpc extends com.raytheon.uf.common.dataplugin.persist.PersistableDataObject
        implements java.io.Serializable, IRawTS {

    private static final long serialVersionUID = 1L;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private RawpcId id;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private String pe;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private short dur;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private Double value;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private String shefQualCode;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private Integer qualityCode;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private Short revision;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private String productId;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private Date producttime;

    @com.raytheon.uf.common.serialization.annotations.DynamicSerializeElement
    private Date postingtime;

    public Rawpc() {
    }

    public Rawpc(RawpcId id, String pe, short dur) {
        this.id = id;
        this.pe = pe;
        this.dur = dur;
    }

    public Rawpc(RawpcId id, String pe, short dur, Double value,
            String shefQualCode, Integer qualityCode, Short revision,
            String productId, Date producttime, Date postingtime) {
        this.id = id;
        this.pe = pe;
        this.dur = dur;
        this.value = value;
        this.shefQualCode = shefQualCode;
        this.qualityCode = qualityCode;
        this.revision = revision;
        this.productId = productId;
        this.producttime = producttime;
        this.postingtime = postingtime;
    }

    @EmbeddedId
    @AttributeOverrides( {
            @AttributeOverride(name = "lid", column = @Column(name = "lid", nullable = false, length = 8)),
            @AttributeOverride(name = "ts", column = @Column(name = "ts", nullable = false, length = 2)),
            @AttributeOverride(name = "extremum", column = @Column(name = "extremum", nullable = false, length = 1)),
            @AttributeOverride(name = "obstime", column = @Column(name = "obstime", nullable = false, length = 29)) })
    public RawpcId getId() {
        return this.id;
    }

    public void setId(RawpcId id) {
        this.id = id;
    }

    @Column(name = "pe", nullable = false, length = 2)
    public String getPe() {
        return this.pe;
    }

    public void setPe(String pe) {
        this.pe = pe;
    }

    @Column(name = "dur", nullable = false)
    public short getDur() {
        return this.dur;
    }

    public void setDur(short dur) {
        this.dur = dur;
    }

    @Column(name = "value", precision = 17, scale = 17)
    public Double getValue() {
        return this.value;
    }

    public void setValue(Double value) {
        this.value = value;
    }

    @Column(name = "shef_qual_code", length = 1)
    public String getShefQualCode() {
        return this.shefQualCode;
    }

    public void setShefQualCode(String shefQualCode) {
        this.shefQualCode = shefQualCode;
    }

    @Column(name = "quality_code")
    public Integer getQualityCode() {
        return this.qualityCode;
    }

    public void setQualityCode(Integer qualityCode) {
        this.qualityCode = qualityCode;
    }

    @Column(name = "revision")
    public Short getRevision() {
        return this.revision;
    }

    public void setRevision(Short revision) {
        this.revision = revision;
    }

    @Column(name = "product_id", length = 10)
    public String getProductId() {
        return this.productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "producttime", length = 29)
    public Date getProducttime() {
        return this.producttime;
    }

    public void setProducttime(Date producttime) {
        this.producttime = producttime;
    }

    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "postingtime", length = 29)
    public Date getPostingtime() {
        return this.postingtime;
    }

    public void setPostingtime(Date postingtime) {
        this.postingtime = postingtime;
    }

    @Override
    @Transient
    public String getLid() {
        return getId().getLid();
    }

    @Override
    @Transient
    public String getTs() {
        return getId().getTs();
    }

    @Override
    @Transient
    public String getExtremum() {
        return getId().getExtremum();
    }

    @Override
    @Transient
    public java.util.Date getObstime() {
        return getId().getObstime();
    }

}

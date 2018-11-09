import React, { Component } from 'react';
import moment from 'moment';

class Job extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    }
  }

  render() {
  	const listItems = this.props.jobs_list.map((d) => 
  		<div className='corners'>
  			<div clsssName='job-container'>
				<div className='job-info'>
					<h2><a href={d.job_url} target='_blank'>{d.company}</a></h2>
					<h2>Category: {d.category}</h2>
					<p>From {moment(d.date_start).format('MMM YYYY')} to {d.date_end ? moment(d.date_end).format('MMM YYYY') : 'now'}</p>
					<p>{d.description}</p>
				</div>
				<div className='job-info'>
					<img name='job' src={"http:\/\/localhost:8000" + d.job_image}/>
				</div>
			</div>
		</div>);

  	return (
  		<div>
  			{listItems}
  		</div>
  		);
  	}
}

export default Job;
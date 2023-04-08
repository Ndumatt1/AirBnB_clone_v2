# This puppet script setup webserver for deployment

class nginx_installation {
  package { 'nginx':
    ensure => installed,
	}
  file {'/data/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode => '0755',
  }

  file {'/data/web_static/':
    ensure => directory,
	mode => '0755',
	owner => 'ubuntu',
	group => 'ubuntu'
  }

  file {'/data/web_static/shared/':
    ensure => directory,
	mode => '0755',
	owner => 'ubuntu',
	group => 'ubuntu',
  }

  file {'/data/web_static/releases/test/':
    ensure => directory,
	mode => '0755',
	owner => 'ubuntu',
	group => 'ubuntu',
  }

  file {'/data/web_static/releases/test/index.html':
    ensure => present,
	content => 'Testing',
    mode => '0644',
	owner => 'ubuntu',
	group => 'ubuntu',
  }
  
  file {'/data/web_static/current':
    ensure => '/data/web_static/releases/test/',
	owner => 'ubuntu',
	group => 'ubuntu',
  }

  file {'/etc/nginx/sites-available/default/':
    ensure => file,
	owner => 'root',
	group => 'root',
	mode => '0644',
	content => template('nginx/default.erb'),
	require => package['nginx'],
	}

	file {'/etc/nginx/sites-enabled/default':
	  ensure => '/etc/nginx/sites-available/default',
	}

	service {'nginx':
	  ensure => 'running',
	  enable => true,
	  subscribe => [ File['/etc/nginx/sites-available/default'], File['/data/web_static/current'] ],
	  }
}  
